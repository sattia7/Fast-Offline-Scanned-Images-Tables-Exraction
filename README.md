# Fast-Offline-Scanned-Images-Tables-Exraction

## 🧬 Hyper-Orchestrated Agentic Pipeline for Scanned Table Intelligence

Enterprise-grade multi-agent system for scanned table extraction using Local Vision-Language Models, LangGraph orchestration, recursive validation, and LangSmith telemetry.

---

## 📌 System Identity

This platform is engineered as a **self-correcting cybernetic perception system** designed to autonomously convert unstructured scanned table imagery into structured, validated, versioned tabular artifacts.

Core attributes:

- Agentic
- Deterministic
- Recursive
- Self-healing
- Traceable
- Modular
- Replaceable

---

## 🧠 Cognitive Architecture

The system operates as a **poly-agent cognitive mesh** where specialized agents collaboratively reason over visual, structural, and semantic representations.

Each agent acts as an autonomous cognitive unit with bounded responsibility and shared state synchronization.


---

## 📥 Input Materialization Phase

1. Raw images placed in `data/raw_images/`.
2. Generate UUID.
3. Compute SHA-256 hash.
4. Create lineage object.
5. Instantiate pipeline state.

   
---

## 🔥 Global Bootstrap Phase

1. Load environment variables.
2. Hydrate configuration graph from `configs/system.yaml`.
3. Compile runtime contracts.
4. Initialize Local VLM memory map.
5. Construct LangGraph topology.
6. Attach LangSmith tracing hooks.
7. Seed deterministic RNG.
8. Initialize telemetry buses.

**Output:**  
A fully instrumented execution substrate.

---

---

## 🧹 Image Pre-Normalization Cascade

This stage transforms raw scanned imagery into a **canonical visual representation** suitable for downstream structural reasoning and vision-language inference.

All operations are executed in a deterministic, chained micro-pipeline.

---

### 3.1 Photometric Stabilization Layer

Purpose: Normalize illumination inconsistencies and enhance contrast distribution.

Operations:

- Gamma equalization  
- Adaptive histogram equalization (CLAHE)  
- Contrast stretching  
- Dynamic range compression  
- White balance correction  
- Color space normalization (RGB → GRAY → LAB)

Output:

- Photometrically stable image tensor

---

### 3.2 Geometric Rectification Layer

Purpose: Eliminate spatial distortions introduced during scanning.

Operations:

- Hough transform based skew angle estimation  
- Rotation correction  
- Perspective homography estimation  
- Quadrilateral projection flattening  
- Border trimming  
- Aspect ratio normalization  

Output:

- Planar-aligned document image

---

### 3.3 Morphological Conditioning Layer

Purpose: Reinforce structural boundaries and suppress artifacts.

Operations:

- Binary thresholding  
- Opening  
- Closing  
- Top-hat transform  
- Skeletonization  
- Multi-kernel erosion and dilation  

Output:

- Structurally reinforced binary mask

---

### 3.4 Noise Attenuation Layer

Purpose: Remove stochastic noise without degrading edges.

Operations:

- Median filtering  
- Bilateral smoothing  
- Non-local means denoising  
- Gaussian smoothing  
- Speckle reduction  

Output:

- Noise-suppressed image tensor

---

### 3.5 Resolution Harmonization Layer

Purpose: Enforce uniform spatial resolution.

Operations:

- DPI estimation  
- Bicubic resampling  
- Super-resolution (optional)  
- Pixel density normalization  

Output:

- Resolution-consistent image

---

### 3.6 Edge Emphasis Layer

Purpose: Enhance table grid visibility.

Operations:

- Sobel gradients  
- Canny edge detection  
- Laplacian sharpening  
- Edge thickening  

Output:

- High-energy edge map

---

## 📐 Table Region Hypothesis Generation

This stage discovers spatially localized regions that are statistically and structurally likely to contain tabular data.  
All computations operate on the **pre-normalized canonical image tensor**.

---

### 4.1 Edge Energy Projection

Purpose: Detect horizontal and vertical line density concentrations.

Operations:

- Compute Sobel-X and Sobel-Y gradients  
- Accumulate gradient magnitudes  
- Generate horizontal projection profile  
- Generate vertical projection profile  
- Smooth projections using Gaussian kernel  
- Detect peaks using local maxima search  

Output:

- Horizontal energy vector  
- Vertical energy vector  

---

### 4.2 Line Structure Extraction

Purpose: Identify dominant straight-line primitives.

Operations:

- Canny edge detection  
- Probabilistic Hough Transform  
- Line orientation clustering  
- Line length thresholding  
- Parallel line grouping  

Output:

- Horizontal line set  
- Vertical line set  

---

### 4.3 Contour Graph Construction

Purpose: Build connected components representing enclosed regions.

Operations:

- Binary mask thresholding  
- Connected component labeling  
- Contour extraction  
- Polygon approximation  
- Hierarchy construction  

Output:

- Contour graph with parent-child relationships  

---

### 4.4 Candidate Bounding Box Synthesis

Purpose: Convert structural primitives into bounding boxes.

Operations:

- Merge intersecting horizontal and vertical lines  
- Compute rectangular hulls  
- Expand hull margins  
- Normalize coordinates  
- Clip to image bounds  

Output:

- Candidate bounding boxes  

---

### 4.5 Candidate Scoring Engine

Each candidate region is scored using multi-factor heuristics.

Scoring Factors:

- Rectangularity ratio  
- Aspect ratio plausibility  
- Internal gridline count  
- Edge density  
- Whitespace balance  
- Text density estimate  

Score Formula (conceptual):

