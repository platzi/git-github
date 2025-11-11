import express from 'express';

const task = {
    name: 'Task API',
    version: '1.0.0',
    description: 'Task API for managing tasks',
};

const router = express.Router();
router.use(express.json());

console.log('Task API');

router.get('/', (_, res) => {
    res.send('Task API');
});

export { router as taskRouter };