<template>
  <div id="categories">
    <div >
      <a-radio-group v-model="value" @change="onChange" class="rbtns" size="large">
        <a-radio-button value="a">
          Cat 1
        </a-radio-button>
        <a-radio-button value="b">
          Cat 2
        </a-radio-button>
        <a-radio-button value="c">
          Cat 3
        </a-radio-button>
        <a-radio-button value="d">
          Cat 4
        </a-radio-button>
      </a-radio-group>
    </div>
    <div id="tags">
      <a-checkable-tag v-model="checked1" @change="handleChange">
        Tag1
      </a-checkable-tag>
      <a-checkable-tag v-model="checked2" @change="handleChange">
        Tag2
      </a-checkable-tag>
      <a-checkable-tag v-model="checked3" @change="handleChange">
        Tag3
      </a-checkable-tag>
    </div>
  </div>

</template>

<script>
    export default {
        name: "category.vue",
      data() {
        return {
          value: 'a',
          checked1: false,
          checked2: false,
          checked3: false,
        };
      },
      methods: {
        onChange(e) {
          console.log(`checked = ${e.target.value}`);
        },
        handleChange(checked) {
          console.log(checked);
        },
      },
    }
</script>

<style scoped>
#categories {
  width: 67%;
  margin: 15px auto;
}
#tags {
  margin-top: 15px;
}
</style>
