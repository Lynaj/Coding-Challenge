/* eslint-disable */
import * as types from './types'
import Vue from 'vue'


/* eslint-disable */
export const GET_current_action = state => state.userObject.currentAction;
export const GET_CURRENCIES = state => state.userObject.CURRENCIES;
export const GET_RECIPIENTS = state => state.userObject.RECIPIENTS;
export const GET_BALANCES = state => state.userObject.BALANCES;

export const state = {
  userObject: {
    loginStatus: false,
    currentAction: '',
    RECIPIENTS: [],
    CURRENCIES: [],
    BALANCES: [],
  }
};

export const mutations = {
  [types.CURRENCIES.SAVE_ALL] (state, { payload }) {
    state.userObject.CURRENCIES = payload;
  },
  [types.RECIPIENTS.SAVE_ALL] (state, { payload }) {
    state.userObject.RECIPIENTS = payload;
  },
  [types.BALANCES.SAVE_ALL] (state, { payload }) {
    state.userObject.BALANCES = payload;
  },

  // AUTHORIZATION
  [types.LOG_USER_IN] (state) {
    state.userObject.loginStatus = USER_LOGIN_STATUS.LOGGED_IN
  },
  [types.LOG_USER_OFF] (state) {
    state.userObject.loginStatus = USER_LOGIN_STATUS.LOGGED_OFF
  },

};
