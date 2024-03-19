<!-- TODO: Declare props and methods -->
<template>
  <div class="search-container">
    <input type="text" v-model="searchQuery" @input="search" placeholder="Search..." />
    <button @click="performSearch">Search</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "SearchBox",
});
</script>

<style>
.search-container {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.search-input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 5px;
}

.search-button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
