import Vue from 'vue'
import Router from 'vue-router'
// import Ping from '../components/Ping'
import Shops from '../components/Shops'
import Malls from '../components/Malls'
import HelloWorld from '../components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/shops',
      name: 'Shops',
      component: Shops
    },
    {
      path: '/malls',
      name: 'Malls',
      component: Malls
    },
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ],
  mode: 'history'
})
