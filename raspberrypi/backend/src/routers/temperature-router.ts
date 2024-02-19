import { Router } from 'express';
import * as temperatureController from '../controllers/temperature-controller';

const router: Router = Router();

router.post('/api/config', temperatureController.modifyConfiguration)

export default router;