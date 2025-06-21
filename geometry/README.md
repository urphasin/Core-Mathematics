# Computational Geometry Learning Plan

## 🔭 Week 1: Foundations of Geometry

**Goal**: Understand basic objects and relationships.

🧠 **Concepts:**
* Points, lines, vectors
* Distance between points
* Angle between vectors
* Dot product, cross product

🐍 **Python:**
* Write functions: `distance(p1, p2)`, `dot(v1, v2)`, `angle(v1, v2)`
* Practice basic vector math with NumPy

🌐 **JavaScript (p5.js):**
* Plot points and lines
* Animate vector rotation or angle display

## 🔺 Week 2: Triangles and Polygons

**Goal**: Work with shapes and their properties.

🧠 **Concepts:**
* Triangle area (Heron's formula, cross product method)
* Polygon area
* Polygon orientation (clockwise/counterclockwise)
* Centroids

🐍 **Python:**
* Implement area functions
* Function to detect polygon orientation

🌐 **p5.js:**
* Draw arbitrary polygons
* Animate centroid calculation

## 🔁 Week 3: Intersections and Containment

**Goal**: Handle shape interaction and querying.

🧠 **Concepts:**
* Line segment intersection
* Point-in-triangle and point-in-polygon (ray casting)
* Bounding boxes

🐍 **Python:**
* Write `doIntersect(seg1, seg2)` and `pointInPolygon(point, poly)`

🌐 **p5.js:**
* Visual demo: Mouse click inside/outside a polygon
* Show ray-casting visually

## 📦 Week 4: Convex Hulls

**Goal**: Solve your first big algorithmic problem!

🧠 **Concepts:**
* Convex hull (Graham scan / Andrew's monotone chain)
* Applications: collision detection, simplification

🐍 **Python:**
* Implement Graham scan or Andrew's algorithm
* Test on sets of random 2D points

🌐 **p5.js:**
* Animate convex hull forming as points are added

## 🧠 Week 5: Advanced Geometry Algorithms

**Goal**: Deepen understanding and explore tough algorithms.

**Topics (pick 2–3):**
* Closest pair of points (divide & conquer)
* Circle intersection
* Sweep line algorithms
* Voronoi diagrams (just the basics)
* Line sweep with event queues

**Optional libraries:**
* `scipy.spatial` for Voronoi in Python
* D3.js for diagrams in the browser