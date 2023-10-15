import React from 'react';
import { Provider } from 'react-redux';
import { applyMiddleware, createStore, compose } from 'redux';
import thunk from 'redux-thunk';

import "~/main/page/main.scss";
import reducers from '@rdx';
import MyMap from '@js/components/MyMap';
import MyMenu from '@js/components/MyMenu';
import Filters from '@js/components/Filters'


const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(reducers,/* devTools для редукса*/ composeEnhancer(applyMiddleware(thunk)));

const AppPage = ({}) => {
  
  return(
    <Provider store={store}>
      <div style={{ position: 'fixed', width: "100vw", height: "100vh", overflowY: 'none' }}>
        <MyMap/>
        <MyMenu/>
        <Filters/>
      </div>
    </Provider>
  );
}

export default AppPage;
