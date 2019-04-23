import requests
import re
import os
import json
import random
import binascii
import PyPDF2
from uuid import uuid4
import io as BytesIO
from base64 import b64decode

from django.db import models
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
# import rest_framework_filters as filters

from apps.users.models import User
from apps.users.serializers import *

from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.decorators import list_route, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework import filters

from backend.apps.transactions.models import *
from backend.apps.transactions.serializers import *

from backend.apps.clients.models import Client
from backend.apps.misc.logger import *

from django.db.models import Q

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser,)

    '''
        * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
        * @description 
         Generates list of transactios processed by the currently logged user
        * @param -
        * @return - queryset
    '''

    def get_queryset(self):

        if self.request.user.is_authenticated:

            queriedClient = get_object_or_404(
                Client.objects.all(),
                userObject=self.request.user
            )

            queryset = Transaction.objects.filter(
                Q(
                    recipient=queriedClient
                )
                |
                Q(
                    sender=queriedClient
                )
            )

        else:
            queryset = Transaction.objects.none()

        return queryset


    @list_route(methods=['POST'])
    def transfer(self, request):

        try:
            queryset = self.get_queryset()
            page = self.request.query_params.get('page', None)
            if page is not None:
                paginate_queryset = self.paginate_queryset(queryset)
                serializer = self.serializer_class(paginate_queryset, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            logger.error(
                "Something unexpected happened when in: CompanyViewSet-data: "
                + '\n'
                + str(e)
            )

        return Response(status=status.HTTP_404_NOT_FOUND)

    @list_route(methods=['POST'])
    def convert(self, request):
        try:

            queryset = self.get_queryset()
            page = self.request.query_params.get('page', None)
            if page is not None:
                paginate_queryset = self.paginate_queryset(queryset)
                serializer = self.serializer_class(paginate_queryset, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            logger.error(
                "Something unexpected happened when in: CompanyViewSet-data: "
                + '\n'
                + str(e)
            )

        return Response(status=status.HTTP_404_NOT_FOUND)
