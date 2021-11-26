let routerimg, cellSize, routers = [];
let map = [
	[null, null, null, null, null, null, null, null],
	[null, null, null, null, null, null, null, null],
	[null, null, null, null, null, null, null, null],
	[null, null, null, null, null, null, null, null],
	[null, null, null, null, null, null, null, null],
	[null, null, null, null, null, null, null, null],
	[null, null, null, null, null, null, null, null],
	[null, null, null, null, null, null, null, null],
]; // null, router, ray

function preload() {
	routerimg = loadImage('router.svg');
}

class Router {
	constructor(x, y) {
		this.pos = createVector(x, y);
		map[this.pos.x][this.pos.y] = 'router';
		this.rays = this.generateRays();
	}

	show() {
		fill('#999');
		rect(this.pos.x * cellSize, this.pos.y * cellSize, cellSize, cellSize);
		image(routerimg, this.pos.x * cellSize + 20, this.pos.y * cellSize + 20, 60, 60);
	}

	generateRays() {
		let rays = [];

		this.posD1 = Object.assign({}, this.pos);
		this.posD2 = Object.assign({}, this.pos);

        for (let steps = 0; steps < 8; steps++) {
			rays.push(createVector(steps, this.pos.y));
			rays.push(createVector(this.pos.x, steps));

			this.posD1.x = (this.posD1.x + 1) % 8
			this.posD1.y = (this.posD1.y + 1) % 8

			if (this.posD1.x - this.posD1.y == this.pos.x - this.pos.y) {
				rays.push(createVector(this.posD1.x, this.posD1.y));
			}

			this.posD2.x = (this.posD2.x + 1) % 8
			this.posD2.y = (this.posD2.y - 1) % 8

			if(!(this.pos.x === 0 && this.pos.y === 0) && !(this.pos.x === 7 && this.pos.y === 7)) {
				if (this.posD2.x - this.posD2.y != 0) {
					if (this.posD2.y < 0) {
						rays.push(createVector(this.posD2.x, 8 - Math.abs(this.posD2.y)));
					} else {
						rays.push(createVector(this.posD2.x, Math.abs(this.posD2.y)));
					}
				}
			}

        }

		for (const ray of rays) {
			map[ray.x][ray.y] = 'ray';
		}

		return rays;
	}
}

function addRouters(index) {
	if(index == 7) {
		console.log("found solution");
		return;
	}

	if(index >= routers.length) routers.push(new Router(0, 0));
	this.router = routers[index];

	for (let i = this.router.pos.x; i < 8; i++) {
		if (!map[i].includes('router')) {
			for (let j = this.router.pos.y; j < 8; j++) {
				if (map[i][j] != 'router' && map[i][j] != 'ray') {
					// console.log(i + " " + j);
					routers.push(new Router(i, j));
					index += 1;
					addRouters(index);
					return;
				}
			}
		}
	}
	if (index <= 0) {
		console.log('no solution');
		return;
	}
	index -= 1;
	addRouters(index);
}

function setup() {
	frameRate(60);
	createCanvas(800, 800);
	background(220);

	cellSize = width / 8;

	for (let i = 0; i < width; i += cellSize) {
		line(i, 0, i, width);
		line(0, i, width, i);
	}
	checkbox = createCheckbox('show all rays', true);

	// routers.push(new Router(5, 3));
	// routers.push(new Router(3, 3));
    // routers.push(new Router(0, 0));
    // routers.push(new Router(0, 7));
    // routers.push(new Router(2, 7));
	addRouters(0);
}

function draw() {
    for (const [x, row] of map.entries()) {
        for (const [y, field] of row.entries()) {
            if (field === 'ray') {
                checkbox.checked() ? fill('#cc0') : fill('#ddd');
                rect(x * cellSize, y * cellSize, cellSize, cellSize);
			}
		}
	}

	for (const router of routers) {
		router.show();
	}
}
