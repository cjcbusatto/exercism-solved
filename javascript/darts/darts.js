export const solve = (x, y) => {
    if (typeof x !== 'number' || typeof y !== 'number') {
        return null;
    }

    const INNER_CIRCLE_RADIUS = 1;
    const MIDDLE_CIRCLE_RADIUS = 5;
    const OUTER_CIRCLE_RADIUS = 10;

    const distanceToCenter = Math.sqrt(x * x + y * y);
    if (distanceToCenter <= INNER_CIRCLE_RADIUS) {
        return 10;
    } else if (distanceToCenter <= MIDDLE_CIRCLE_RADIUS) {
        return 5;
    } else if (distanceToCenter <= OUTER_CIRCLE_RADIUS) {
        return 1;
    } else {
        return 0;
    }
};
