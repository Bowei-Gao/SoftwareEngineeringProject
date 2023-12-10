<template>
  <div  id="pagination">
    <a-pagination id="subpage" show-quick-jumper :default-current="1" :total="500" @change="onChange" />
  </div>
</template>

<script>
  export default {
    methods: {
      onChange(pageNumber) {
        console.log('Page: ', pageNumber);
      },
    },
  };
</script>

<style scoped>
#pagination {
  width: 67%;
  margin: 15px auto 0;
  justify-content: center;
  display: flex;
}
  #subpage {
    vertical-align: middle;
  }
</style>
