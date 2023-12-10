<template>
    <div class="mainbar">
      <a-menu mode="horizontal" :default-selected-keys="['1']">
        <a-menu-item id="person" key="1"><a-icon type="bell" />个人提醒</a-menu-item>
        <a-menu-item key="2"><a-icon type="flag" />我的主题</a-menu-item>
        <a-menu-item key="3"><a-icon type="retweet" />我的回复</a-menu-item>
        <a-menu-item key="4"><a-icon type="issues-close" />举报提醒</a-menu-item>
      </a-menu>
      <div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "mainpageBar.vue",
        mounted () {
        axios
         .get('https://www.runoob.com/try/ajax/json_demo.json')
         .then(response => (getElementById("person").value = response))
         .catch(function (error) { // 请求失败处理
        console.log(error);
        });
  }
    }
</script>

<style scoped>
.mainbar {
  width: 67%;
  margin: 15px auto 0;
}
</style>
