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
];

function preload() {
	routerimg = loadImage('router.svg');
}

class Router {
	constructor(x, y) {
		this.pos = createVector(x, y);
		this.rays = this.generateRays();
		map[this.pos.x][this.pos.y] = this;
		this.show_rays = true;
		this.index = routers.length;
	}

	show() {
		fill('#999');
		rect(this.pos.x * cellSize, this.pos.y * cellSize, cellSize, cellSize);
		image(routerimg, this.pos.x * cellSize + 20, this.pos.y * cellSize + 20, 60, 60);
		fill(0);
		textSize(18);
		textStyle(BOLD);
		text(this.index, this.pos.x * cellSize + 80, this.pos.y * cellSize + 90);
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
		}

		let diagonalCount = this.pos.x + this.pos.y
		if (diagonalCount > 7) {
			diagonalCount = 7 - (diagonalCount % 7);
		}
		if (diagonalCount % 2 != 0) {
			rays.push(createVector(this.posD2.y, this.posD2.x));
		}

		if (this.pos.x === this.pos.y) {
			for (let steps = 0; steps < Math.ceil(diagonalCount / 2); steps++) {
				this.posD2.x = (this.posD2.x + 1) % 8;
				this.posD2.y = (this.posD2.y - 1) % 8;
				if (this.posD2.y < 0) {
					rays.push(createVector(this.posD2.x, 8 + this.posD2.y));
					rays.push(createVector(8 + this.posD2.y, this.posD2.x));
				} else {
					rays.push(createVector(this.posD2.x, this.posD2.y));
					rays.push(createVector(this.posD2.y, this.posD2.x));
				}
			}
		} else {
			for (let steps = 0; steps < diagonalCount; steps++) {
				this.posD2.x = (this.posD2.x + 1) % 8;
				this.posD2.y = (this.posD2.y - 1) % 8;
				if (this.posD2.y < 0) {
					rays.push(createVector(this.posD2.x, 8 + this.posD2.y));
					rays.push(createVector(8 + this.posD2.y, this.posD2.x));
				} else {
					rays.push(createVector(this.posD2.x, this.posD2.y));
					rays.push(createVector(this.posD2.y, this.posD2.x));
				}
			}
		}


		for (const ray of rays) {
			if (map[ray.x][ray.y] instanceof Ray) {
				map[ray.x][ray.y].routers.push(this);
			} else {
				map[ray.x][ray.y] = new Ray(this, ray.x, ray.y);
			}
		}

		return rays;
	}
}

class Ray {
	constructor(router, x, y) {
		this.routers = [router];
		this.pos = createVector(x, y);
	}

	show() {
		fill('#ddd');
		for (const router of this.routers) {
			if (router.show_rays) {
				fill('#cc0');
				break;
			} else {
				fill('#ddd');
			}
		}
		rect(this.pos.x * cellSize, this.pos.y * cellSize, cellSize, cellSize);
	}
}

Array.prototype.includesObject = function (object) {
	for (const element of this) {
		if (element instanceof object) return true;
	}
	return false;
}

function addRouters(index) {
	// index = routers.length;
	if (index == 7) {
		console.log('solution found');
		return;
	}

	if (index >= routers.length) {
		routers.push(new Router(0, 0));
		map[0][0] = new Router(0, 0);
	}

	this.router = routers[index];

	for (let i = this.router.pos.x; i < 8; i++) {
		if (!map[i].includesObject(Router)) {
			for (let j = this.router.pos.y; j < 8; j++) {
				if (!(map[i][j] instanceof Router) && !(map[i][j] instanceof Ray)) {
					routers.push(new Router(i, j));
					map[i][j] = new Router(i, j);
					addRouters(index++);
					return;
				}
			}
		}
	}
	if (index == 0) {
		return;
	}
	// routers.pop();
	addRouters(index--);
	return;
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
	checkbox.changed(() => {
		for (const row of map) {
			for (const field of row) {
				if (field instanceof Router) {
					field.show_rays = checkbox.checked();
				}
			}
		}
	});

	// map[3][4] = new Router(3, 4);
	// map[4][3] = new Router(4, 3);
	// map[4][4] = new Router(4, 4);
	// map[5][5] = new Router(5, 5);
	// map[5][2] = new Router(5, 2);

	addRouters(0);
	for (const router of routers) {
		map[router.pos.x][router.pos.y] = router;
	}
}

function draw() {
    for (const row of map) {
        for (const field of row) {
            if (field instanceof Ray) {
				field.show();
			}
		}
	}
	for (const row of map) {
        for (const field of row) {
            if (field instanceof Router) {
				field.show();
			}
		}
	}
}

function mouseClicked(event) {
	this.x = int((event.clientX - 8) / cellSize);
	this.y = int((event.clientY - 8) / cellSize);
	if (0 <= this.x && this.x < 8 && 0 <= this.y && this.y < 8) {
		field = map[this.x][this.y]
		if (field instanceof Router) {
			field.show_rays = !field.show_rays;
		}
	}
}
