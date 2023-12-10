<template>
    <a-layout id="layout-header">
      <a-layout-header class="myheader">
        <div class="headerbox">
        <div class="logo" />
          <a-menu theme="dark"
                  mode="horizontal"
                  :default-selected-keys="['1']"
                  :style="{ lineHeight: '64px' }"
                  >
            <a-menu-item key="1" @click="clickA">
              个人主页
            </a-menu-item>
            <a-menu-item key="2" @click="clickB">
              主题
            </a-menu-item>
            <a-menu-item key="3" @click="clickC">
              匿名主题
            </a-menu-item>
          </a-menu>
        </div>
      </a-layout-header>
    </a-layout>
</template>

<script>
  export default {
    name: "myheader",
    data () {
      return {
        collapsed: false,
      }
    },
    methods: {
      clickA: function () {
        console.log('Highest menu 1 clicked')
        this.$emit('clickMenuA')
      },
      clickB: function () {
        console.log('Highest menu 2 clicked')
        this.$emit('clickMenuB')
      },
      clickC: function () {
        console.log('Highest menu 3 clicked')
        this.$emit('clickMenuC')
      }
    }
  }
</script>

<style scoped>
  .headerbox {
    width: 67%;
    margin: 0 auto;
  }
#layout-header .logo {
  width: 120px;
  height: 31px;
  background: rgba(255,255,255,0.2);
  margin: 16px 28px 16px 0;
  float: left;
}
</style>
