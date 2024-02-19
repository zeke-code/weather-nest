<script lang="ts">
import { defineComponent } from 'vue';
import Chart from 'chart.js/auto';

export default defineComponent({
    data() {
        return {
            // You can place other component data here
        };
    },
    methods: {
        createChart(chartId: string) {
            const canvas = document.getElementById(chartId) as HTMLCanvasElement;
            const ctx = canvas.getContext('2d');

            if (ctx) {
                new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['8 AM', '10 AM', '12 PM', '2 PM', '4 PM', '6 PM'],
                    datasets: [{
                        label: 'Temperature (°C)',
                        data: [16, 18, 20, 22, 19, 17],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
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
        },
    },
    mounted() {
        this.createChart('temperatureChart');
    }
})
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
