import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { FirstComp, SeconComp } from './index';

const Router = () => (
  <Switch>
    <Route exact path = "/" component={FirstComp} />
    <Route exact path = "/changed/" component={SeconComp} />
  </Switch>
);

export default Router;