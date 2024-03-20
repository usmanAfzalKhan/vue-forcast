<template>
  <div class="secondary-view">
    <span class="day-time">Sunday</span>
    <span class="temp-num">11&deg;</span>
    <span class="weather-type">Sunny</span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "WeatherDisplayMini",
});
</script>

<style>
.secondary-view {
  border: 2px solid #e0e0e0;
  display: flex;
  flex-direction: column;
  padding: 24px 12px;
  border-radius: 16px;

  .day-time {
    font-size: 2vmin;
  }
  .temp-num {
    font-size: 4vmin;
  }
  .weather-type {
    font-size: 2vmin;
  }
}
</style>
