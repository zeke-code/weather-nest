<script lang="ts">
import { defineComponent } from 'vue';
import Chart from 'chart.js/auto';
import axios from 'axios';

interface TemperatureData {
    timestamp: string;
    temperature: number;
}

export default defineComponent({
    data() {
        return {
            chart: null,
            temperatureData: [] as TemperatureData[]
        };
    },
    methods: {
        async fetchTemperatureData() {
            try {
                const response = await axios.get('/api/temperatures/today');
                this.temperatureData = response.data;
                this.updateChartData();
            } catch (error) {
                console.error('Failed to fetch temperature data', error);
            }
        },
        updateChartData() {
            this.temperatureData.sort((a, b) => new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime());

            const labels = this.temperatureData.map(data => {
                const date = new Date(data.timestamp);
                const hours = date.getHours().toString().padStart(2, '0');
                const minutes = date.getMinutes().toString().padStart(2, '0');
                return `${hours}:${minutes}`;
            });
            const temperatures = this.temperatureData.map(data => data.temperature);
        
            if (this.chart) {
                const chart = this.chart as Chart;
                chart.data.labels = labels;
                chart.data.datasets[0].data = temperatures;
                chart.update();
            } else {
                this.createChart('temperatureChart', labels, temperatures);
            }
        },
        createChart(chartId: string, labels: string[], data: number[]) {
            const canvas = document.getElementById(chartId) as HTMLCanvasElement;
            const ctx = canvas.getContext('2d');

            if (ctx) {
                (this.chart as any) = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Temperature (°C)',
                            data: data,
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        },
                        responsive: true
                    }
                });
            }
        }
    },
    mounted() {
        this.fetchTemperatureData();
    }
});

</script>

<template>
    <div class="container text-center">
        <div class="row">
            <div class="col-12">
                <h1 class="mt-4">Hey, welcome back to Weather Nest!</h1>
                <h2>Here are the temperatures of today</h2>
                <canvas class="mt-4" id="temperatureChart"></canvas>
            </div>
        </div>
    </div>
</template>

<style lang="scss">

</style>
