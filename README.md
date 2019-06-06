## installing with https on AWS:


#### Updating the system
sudo apt-get update
sudo apt-get install build-essential


#### Installing Brew
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
```

#### Installing certbot:

```
brew install certbot
```

#### Creating hook script
```
aws route53 wait resource-record-sets-changed --id \
    $(aws route53 change-resource-record-sets --hosted-zone-id \
        "$(aws route53 list-hosted-zones-by-name --dns-name $2. \
        --query HostedZones[0].Id --output text)" \
      --query ChangeInfo.Id \
      --output text \
      --change-batch "{ \
        \"Changes\": [{ \
          \"Action\": \"$1\", \
          \"ResourceRecordSet\": { \
            \"Name\": \"_acme-challenge.${CERTBOT_DOMAIN}.\", \
            \"ResourceRecords\": [{\"Value\": \"\\\"${CERTBOT_VALIDATION}\\\"\"}], \
            \"Type\": \"TXT\", \
            \"TTL\": 30 \
          } \
        }] \
      }" \
    )
```

#### This will create an executable script that uses the AWS CLI to insert a TXT record in your Route53 DNS records.
```
wget https://gist.githubusercontent.com/li0nel/4563f8d909e808169c91a5521569ff10/raw/cb1396d07eb91700642b27a4cd92e335498c03ca/auth-hook.sh -O ./auth-hook.sh && chmod +x auth-hook.sh
```

#### Execute Certbot
>In the same directory, execute the below command, after replacing your_domain.com by your actual domain name and the email by your appropriate email address. Note that this will generate a certificate both for your_domain.com and www.your_domain.com. You can add as many subdomains AFAIK however Let’s Encrypt does not support wildcard certificates.
```
certbot certonly --non-interactive --manual \
  --manual-auth-hook "./auth-hook.sh UPSERT your_domain.com" \
  --manual-cleanup-hook "./auth-hook.sh DELETE your_domain.com" \
  --preferred-challenge dns \
  --config-dir "./letsencrypt" \
  --work-dir "./letsencrypt" \
  --logs-dir "./letsencrypt" \
  --agree-tos \
  --manual-public-ip-logging-ok \
  --domains your_domain.com,www.your_domain.com \
--email your@email.com
```

>This might take a couple minutes, but eventually your certificates will be created in a /letsencrypt directory.
>For Nginx, the ssl_certificate file you are looking for is fullchain.pem and the ssl_certificate_key is privkey.pem .






DOCS:
[https://hackernoon.com/easy-lets-encrypt-certificates-on-aws-79387767830b](https://hackernoon.com/easy-lets-encrypt-certificates-on-aws-79387767830b)
[https://docs.brew.sh/Homebrew-on-Linux](https://docs.brew.sh/Homebrew-on-Linux)
