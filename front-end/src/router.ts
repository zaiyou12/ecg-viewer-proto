import { createRouter, createWebHistory, RouteParams } from 'vue-router'

import Home from './pages/Home.vue'
import TestList from './pages/TestList.vue'

export type AppRouteNames = 'home'
| 'testList'

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      name: 'home',
      path: '/',
      component: Home,
    },
    {
      name: 'testList',
      path: '/test-list',
      component: TestList,
    },
    {
      name: 'testViewer',
      path: '/test-list/:index',
      component: () => import('./pages/TestViewer.vue'),
      props: true
    }
  ]
})
