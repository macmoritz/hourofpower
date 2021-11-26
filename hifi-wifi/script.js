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
		map[this.pos.x][this.pos.y] = this;
		this.rays = this.generateRays();
		this.show_rays = false;
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
				console.log(router);
				fill('#cc0');
				break;
			} else {
				fill('#ddd');
			}
		}
		rect(this.pos.x * cellSize, this.pos.y * cellSize, cellSize, cellSize);
	}
}

function addRouters(index) {
	if (index == 7) {
		console.log("found solution");
		return;
	}
	if (index >= routers.length) {
		routers.push(new Router(0, 0));
		map[0][0] = new Router(0, 0);
	}

	this.router = routers[index];

	for (let i = this.router.pos.x; i < 8; i++) {
		if (!map[i].includes(Router)) {
			for (let j = this.router.pos.y; j < 8; j++) {
				if (!(map[i][j] instanceof Router) && !(map[i][j] instanceof Ray)) {
					routers.push(new Router(i, j));
					map[i][j] = new Router(i, j);
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
	// routers.pop();
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

	checkbox = createCheckbox('show all rays', false);
	checkbox.changed(() => {
		for (const row of map) {
			for (const field of row) {
				if (field instanceof Router) {
					field.show_rays = checkbox.checked();
				}
			}
		}
	});

	// routers.push(new Router(5, 3));
	// routers.push(new Router(3, 3));
    // routers.push(new Router(0, 0));
    // routers.push(new Router(0, 7));
    // routers.push(new Router(2, 7));
	addRouters(0);
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
	if (0 < this.x && this.x < 8 && 0 < this.y && this.y < 8) {
		field = map[this.x][this.y]
		if (field instanceof Router) {
			field.show_rays = !field.show_rays;
		}
	}
}
