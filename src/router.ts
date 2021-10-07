import { createRouter, createWebHistory, RouteParams } from 'vue-router'

import LoginPage from '@/pages/LoginPage.vue'
import MainPage from '@/pages/MainPage.vue'
import DashboardPage from '@/pages/DashboardPage.vue'
import TestListPage from '@/pages/TestListPage.vue'
import TestList from '@/components/TestList/index.vue'
import Pagination from '@/components/Pagination/index.vue'
import TestViewPage from '@/pages/TestViewPage.vue'
import EmptyPage from '@/pages/EmptyPage.vue'
import SandboxPage from '@/pages/SandboxPage.vue'

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
      path: '/main',
      component: MainPage,
      redirect: '/main/dashboard',
      children: [
        {
          name: 'dashboard',
          path: 'dashboard',
          component: DashboardPage
        },
        {
          name: 'tests',
          path: 'tests',
          redirect: '/main/tests/1',
          component: TestListPage,
          children: [
            {
              name: 'testPagination',
              path: ':page',
              components: {
                testList: TestList,
                pagination: Pagination
              },
              props: true
            }
          ]
        },
        {
          name: 'testView',
          path: 'view/:testSeq',
          component: TestViewPage,
          props: true
        },
        {  // TODO: Remove later
          name: 'sandbox',
          path: 'sandbox',
          component: SandboxPage,
        }
      ]
    },
    {
      name: 'notFound',
      path: '/:catchAll(.*)',
      component: EmptyPage
    }
  ]
})
