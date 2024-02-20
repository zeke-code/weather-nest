import { Router } from 'express';
import * as temperatureController from '../controllers/temperature-controller';

const router: Router = Router();

router.post('/api/config', temperatureController.modifyConfiguration)
router.get('/api/temperatures/all', temperatureController.getTemperatures);
router.get('/api/temperatures/today', temperatureController.getTodayTemperatures);

export default router;