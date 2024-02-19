import { Router } from 'express';
import * as temperatureController from '../controllers/temperature-controller';

const router: Router = Router();

router.get('/api/test', temperatureController.modifyConfiguration)

export default router;