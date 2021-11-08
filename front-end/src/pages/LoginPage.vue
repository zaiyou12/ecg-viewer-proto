<template>
  <div class="login-page-container">
    <div class="w-1/2 bg-blue-100 flex items-center justify-center">
      <div class="font-bold text-3xl">ECG Viewer Proto</div>
    </div>
    <div class="w-1/2 h-full flex flex-col items-center justify-center">
      <h1 class="font-bold text-3xl cursor-default select-none">Login</h1>
      <div class="w-1/2 h-56 flex flex-col it justify-center">
        <p>Email or ID</p>
        <input type="email" />
        <p>Password</p>
        <input type="password" />
        <!-- <button>LOGIN</button> -->
        <AppLink name="main" class="login-page-container-btn">LOGIN</AppLink>
      </div>
    </div>
  </div>
</template>

<style>
@layer components {
  .login-page-container {
    @apply w-screen h-screen overflow-hidden flex;
  }

  .login-page-container p {
    @apply text-left text-sm cursor-default select-none;
  }

  .login-page-container input {
    @apply w-full h-10 rounded-xl px-4 my-2 block
    text-sm hover:bg-gray-50
    bg-gray-100 focus:outline-none;
  }

  .login-page-container-btn {
    @apply h-10 rounded-lg my-2 py-2.5
    font-bold text-white bg-red-400 text-sm
    hover:bg-red-300;
  }
}
</style>
