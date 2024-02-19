<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
    data() {

    },
    methods: {
        async submitForm(event: Event) {
            event.preventDefault();
            const response = await axios.get('/api/test');
            if (response.status === 200) {
                alert('Test was successful!');
            }
        }
    },
    mounted() {

    }
})
</script>

<template>
    <div class="container">
        <div class="row">
            <div class="col-6 mx-auto">
                <form class="mt-5" @submit="submitForm">
                    <div class="mb-3">
                    <label for="delay" class="form-label">Delay (ms)</label>
                    <input type="number" class="form-control" id="delay" aria-describedby="delayHelp">
                    <div id="delayHelp" class="form-number">Insert the delay (in ms) between measurements here.</div>
                    </div>
                    <div class="mb-3">
                    <label for="temperatureOffset" class="form-label">Temperature Offset</label>
                    <input type="number" class="form-control" aria-describedby="temperatureOffsetHelp" id="temperatureOffset">
                    <div id="temperatureOffsetHelp" class="form-number">Insert the temperature offset here.</div>
                    </div>
                    <label for="humidityOffset" class="form-label">Humidity Offset</label>
                    <input type="number" class="form-control" aria-describedby="humidityOffsetHelp" id="humidityOffset">
                    <div id="humidityOffsetHelp" class="form-number">Insert the humidity offset here.</div>
                    <button type="submit" class="btn btn-primary mt-2">Submit</button>
                </form>
            </div>
        </div>
    </div>
</template>