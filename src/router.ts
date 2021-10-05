import { createRouter, createWebHistory, RouteParams } from 'vue-router'

import LoginPage from '@/pages/LoginPage.vue'
import MainPage from '@/pages/MainPage.vue'
import DashboardPage from '@/pages/DashboardPage.vue'
import TestListPage from '@/pages/TestListPage.vue'
import EmptyPage from '@/pages/EmptyPage.vue'

export type AppRouteNames = 'index' |'login' | 'main'

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      name: 'index',
      path: '/',
      redirect: { name: 'login' }  // TODO: Remove later
    },
    {
      name: 'login',
      path: '/login',
      component: LoginPage
    },
    {
      name: 'main',
      path: '/auth',
      component: MainPage,
      redirect: '/auth/dashboard',
      children: [
        {
          path: 'dashboard',
          components: {
            dashboard: DashboardPage
          }
        },
        {
          path: 'tests',
          components: {
            tests: TestListPage
          }
        }
      ]
    },
    {
      name: 'notFound',
      path: '/:catchAll(.*)',
      component: EmptyPage
    }
    // {
    //   name: 'testViewer',
    //   path: '/test-list/:index',
    //   component: () => import('./pages/TestViewer.vue'),
    //   props: true
    // }
  ]
})
