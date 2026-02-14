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

## 📥 Input Materialization Phase

1. Raw images placed in `data/raw_images/`.
2. Generate UUID.
3. Compute SHA-256 hash.
4. Create lineage object.
5. Instantiate pipeline state.

### Pipeline State Schema

```json
{
  "image_blob": null,
  "lineage_id": "uuid",
  "stage_pointer": "preprocess",
  "retry_counter": 0,
  "entropy_score": 0.0,
  "confidence_vector": [],
  "table_object": null,
  "validation_flags": {}
}



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

### 3.7 Pre-Normalization Output Contract

```json
{
  "image_tensor": "<normalized_tensor>",
  "height": 2048,
  "width": 2048,
  "channels": 1,
  "quality_score": 0.97
}

