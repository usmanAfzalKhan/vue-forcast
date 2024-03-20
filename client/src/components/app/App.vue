<template>
  <SearchBox />
  <WeatherDisplay />
  <div>
    <Button label="Conversion"> </Button>
  </div>
</template>

<script lang="ts">
import Button from "primevue/button";
import { defineComponent } from "vue";
import SearchBox from "../search-box/SearchBox.vue";
import WeatherDisplay from "../weather-display/WeatherDisplay.vue";

export default defineComponent({
  name: "App",
  components: {
    SearchBox,
    WeatherDisplay,
    Button,
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
