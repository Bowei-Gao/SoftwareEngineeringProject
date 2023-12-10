<template>
    <a-layout id="msg">

      <a-layout-sider :class="topicMode" theme="light" v-model="collapsed" :trigger="null" collapsible reverse-arrow id="sidebar">

        <div id="buttomholder" v-if="topicMode==='clear'">
          <a-button id="publish" type="primary" @click="clickCreate"><a-icon type="edit"/>发表新主题</a-button>
        </div>
        <a-divider v-if="topicMode==='clear'"></a-divider>
        <div id="abuttomholder" v-if="topicMode==='anonymous'">
          <a-button id="apublish" type="primary" @click="clickCreate"><a-icon type="edit" />发表新主题</a-button>
        </div>
        <a-divider v-if="topicMode==='anonymous'"></a-divider>
        <a-menu theme="light" v-if="topicMode==='clear'" mode="inline" :default-selected-keys="['1']">
          <a-menu-item key="1">
            <span>全部</span>
          </a-menu-item>
          <a-menu-item key="2">
            <span>Example Category 1</span>
          </a-menu-item>
          <a-menu-item key="3">
            <span>Example Category 2</span>
          </a-menu-item>
          <a-menu-item key="4" @click="clickShowCategory">
            <span>全部分类</span>
          </a-menu-item>
        </a-menu>
        <a-menu theme="dark" v-if="topicMode==='anonymous'" mode="inline" :default-selected-keys="['1']">
          <a-menu-item key="1">
            <span>全部</span>
          </a-menu-item>
          <a-menu-item key="2">
            <span>Example Category 1</span>
          </a-menu-item>
          <a-menu-item key="3">
            <span>Example Category 2</span>
          </a-menu-item>
          <a-menu-item key="4" @click="clickShowCategory">
            <span>全部分类</span>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout-content>
      </a-layout-content>
    </a-layout>

</template>

<script>
  export default {
    name: "msgSidebar.vue",
    props: {
      topicMode: String,
    },
    methods: {
      clickShowCategory: function () {
        console.log('Button show category clicked')
        this.$emit('clickShowCategory')
      },
      clickCreate: function () {
        console.log('Button create topic clicked')
        this.$emit('clickCreate')
      }
    }
  }
</script>

<style scoped>
  #buttomholder {
    margin: 15px auto 15px;
    text-align: center;
  }
  #abuttomholder {
    margin: 15px auto 15px;
    text-align: center;
  }
  .anonymous {
    background-color: #001529;
  }
#msg {
  width: 67%;
  margin: 15px auto 0;
}
</style>
