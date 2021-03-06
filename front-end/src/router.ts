import { createRouter, createWebHistory } from 'vue-router'

import LoginPage from '@/pages/LoginPage.vue'
import MainPage from '@/pages/MainPage.vue'
import DashboardPage from '@/pages/DashboardPage.vue'
import TestListPage from '@/pages/TestListPage.vue'
import TestViewPage from '@/pages/TestViewPage.vue'
import PreprocessPage from '@/pages/PreprocessPage.vue'
import TestGroupPage from '@/pages/TestGroupPage.vue'
import SampleGroupPage from '@/pages/SampleGroupPage.vue'
import EmptyPage from '@/pages/EmptyPage.vue'

export type AppRouteNames = 'index' | 'login' | 'main'

declare module 'vue-router' {
  interface RouteMeta {
    isAdmin?: boolean
    requiresAuth?: boolean
  }
}

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      name: 'index',
      path: '/',
      redirect: { name: 'login' } // TODO: Remove later
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
      meta: { requiresAuth: true },
      beforeEnter: (to, from) => {
        // TODO: Fix later
        if (from.name !== 'login') return true
        if (to.meta.requiresAuth) {
          return true
        }
        return true
      },
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
          component: TestListPage
        },
        {
          name: 'testView',
          path: 'view',
          component: TestViewPage
        },
        {
          name: 'preprocess',
          path: 'preprocess',
          component: PreprocessPage
        },
        {
          name: 'testGroup',
          path: 'test-group',
          component: TestGroupPage
        },
        {
          name: 'sampleGroup',
          path: 'sample-group',
          component: SampleGroupPage
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
