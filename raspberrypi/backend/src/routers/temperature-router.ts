import { Router } from 'express';
import * as temperatureController from '../controllers/temperature-controller';

const router: Router = Router();

router.post('/api/config', temperatureController.modifyConfiguration)
router.get('/api/retrievetemperatures', temperatureController.getTemperatures);

export default router;