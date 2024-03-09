<template>
  <SearchBox/>
  <WeatherDisplay/>
</template>

<script>
import SearchBox from './components/search-box/SearchBox.vue';
import WeatherDisplay from './components/weather-display/WeatherDisplay.vue';

export default {
  name: 'App',
  components: {
    SearchBox,
    WeatherDisplay
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
