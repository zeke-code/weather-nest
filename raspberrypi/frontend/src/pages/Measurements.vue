<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios';

interface Measurement {
    id: number;
    temperature: number;
    humidity: number;
    timestamp: string;
}

export default defineComponent({
    data() {
        return {
            measurements: [] as Measurement[],
            shownMeasurements: [] as Measurement[],
            temperatureFilter: { min: null, max: null },
            humidityFilter: { min: null, max: null },
            timeFilter: { start: null, end: null }
        }
    },
    methods: {
        async fetchData() {
            const response = await axios.get('/api/temperatures/all');
            this.measurements = response.data;
            this.shownMeasurements = [...this.measurements];
        },
        submitForm(e: Event) {
            e.preventDefault();
            this.filterMeasurements();
        },
        filterMeasurements() {
        let filtered = this.measurements.filter(m => {
            const temperatureCondition = (this.temperatureFilter.min === null || m.temperature >= this.temperatureFilter.min) && 
                                         (this.temperatureFilter.max === null || m.temperature <= this.temperatureFilter.max);
            const humidityCondition = (this.humidityFilter.min === null || m.humidity >= this.humidityFilter.min) && 
                                      (this.humidityFilter.max === null || m.humidity <= this.humidityFilter.max);

            let timeCondition = true; // Assume true unless both start and end times are provided
            if (this.timeFilter.start && this.timeFilter.end) {
                const startTime = new Date(this.timeFilter.start).getTime();
                const endTime = new Date(this.timeFilter.end).getTime();
                const measurementTime = new Date(m.timestamp).getTime();
                timeCondition = measurementTime >= startTime && measurementTime <= endTime;
            }

            return temperatureCondition && humidityCondition && timeCondition;
        });

        this.shownMeasurements = filtered;
    },
        formatTemperature(value: number) {
            return Number(value).toFixed(2);
        },
        
        formatDate(timestamp: string) {
            const date = new Date(timestamp);
            return date.toLocaleString();
        }
    },
    mounted() {
        this.fetchData();
    },
})

</script>

<template>
    <div class="container">
        <div class="row">
            <div class="col-6 mx-auto">
                <table class="table table-striped mt-5">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Temperature (°C)</th>
                            <th scope="col">Humidity (%)</th>
                            <th scope="col">Timestamp</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(entry, index) in shownMeasurements" :key="entry.id">
                            <th scope="row">{{ index + 1 }}</th>
                            <td>{{ formatTemperature(entry.temperature) }}</td>
                            <td>{{ entry.humidity }}</td>
                            <td>{{ formatDate(entry.timestamp) }}</td>
                        </tr>
                    </tbody>
                </table>
                <form class="mt-5" @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label for="minTemp" class="form-label">Min Temperature (°C)</label>
                        <input type="number" class="form-control" id="minTemp" v-model="temperatureFilter.min">
                        <div id="minTempHelp" class="form-text">Insert the minimum temperature value.</div>
                    </div>
                    <div class="mb-3">
                        <label for="maxTemp" class="form-label">Max Temperature (°C)</label>
                        <input type="number" class="form-control" id="maxTemp" v-model="temperatureFilter.max">
                        <div id="maxTempHelp" class="form-text">Insert the maximum temperature value.</div>
                    </div>
                    <div class="mb-3">
                        <label for="minHumidity" class="form-label">Min Humidity (%)</label>
                        <input type="number" class="form-control" id="minHumidity" v-model="humidityFilter.min">
                        <div id="minHumidityHelp" class="form-text">Insert the minimum humidity value.</div>
                    </div>
                    <div class="mb-3">
                        <label for="maxHumidity" class="form-label">Max Humidity (%)</label>
                        <input type="number" class="form-control" id="maxHumidity" v-model="humidityFilter.max">
                        <div id="maxHumidityHelp" class="form-text">Insert the maximum humidity value.</div>
                    </div>
                    <div class="mb-3">
                        <label for="startTime" class="form-label">Start Time</label>
                        <input type="datetime-local" class="form-control" id="startTime" v-model="timeFilter.start">
                        <div id="startTimeHelp" class="form-text">Select the start time for filtering.</div>
                    </div>
                    <div class="mb-3">
                        <label for="endTime" class="form-label">End Time</label>
                        <input type="datetime-local" class="form-control" id="endTime" v-model="timeFilter.end">
                        <div id="endTimeHelp" class="form-text">Select the end time for filtering.</div>
                    </div>
                    <button type="submit" class="btn btn-primary mt-2">Filter</button>
                </form>
            </div>
        </div>
    </div>
</template>
