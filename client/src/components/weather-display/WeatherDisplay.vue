<template>
  <h1>City</h1>
  <p>Description</p>
  <div class="weather-display">
    <table class="weather-display-table">
      <tr>
        <th class="weather-display-table-header">Temperature</th>
        <th class="weather-display-table-header">Feels Like</th>
        <th class="weather-display-table-header">Maximum Temperature</th>
        <th class="weather-display-table-header">Minimum Temperature</th>
      </tr>
      <tr>
        <td>15</td>
        <td>14</td>
        <td>12</td>
        <td>6</td>
      </tr>
    </table>
    <table class="weather-display-table">
      <tr>
        <th class="weather-display-table-header">Pressure</th>
        <th class="weather-display-table-header">Humility</th>
        <th class="weather-display-table-header">Degrees</th>
        <th class="weather-display-table-header">Wind Speed</th>
      </tr>
      <tr>
        <td>60</td>
        <td>75</td>
        <td>250</td>
        <td>75</td>
      </tr>
    </table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "WeatherDisplay",
});
</script>

<style scoped>
.weather-display {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

.weather-display-table {
  width: 100%;
}

.weather-display-table-header {
  width: 25%;
}
</style>
