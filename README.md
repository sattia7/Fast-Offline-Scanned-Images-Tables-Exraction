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

---

## 👁 Vision-Language Inference Phase

This phase converts spatially localized table-region imagery into structured symbolic representations using a Local Vision-Language Model (VLM).  
Each region is processed in complete isolation, yet retains lineage binding to the parent document.

---

### 5.1 Visual Embedding Generation Layer

Purpose: Transform pixel space into semantic embedding space.

Operations:

- Patch extraction and tokenization  
- Positional encoding injection  
- Spatial layout embedding  
- Vision backbone forward propagation  
- Feature pyramid aggregation  

Output:

- Dense visual embedding tensor

---

### 5.2 Prompt Assembly Layer

Purpose: Construct a context-rich instruction bundle.

Prompt Stack:

<System Prompt> <Region Metadata Prompt> <Table Extraction Instruction Prompt> <Layout Awareness Prompt> <OCR Correction Prompt> <Validation Hint Prompt> 

Dynamic Variables:

- Region coordinates

- Estimated rows/columns

- Previous failure reasons (if retry)

---

### 5.3 Cross-Modal Fusion

Purpose: Integrate heterogeneous modality representations into a single unified latent manifold suitable for autoregressive reasoning.

---

#### 5.3.1 Visual Token Projection

- Project visual embeddings into language token dimensionality  
- Apply linear transformation and normalization  
- Preserve spatial index metadata  

Output:

- Projected visual token sequence

---

#### 5.3.2 Textual Token Preparation

- Tokenize composite prompt  
- Inject special control tokens  
- Apply positional encodings  

Output:

- Prompt token sequence

---

#### 5.3.3 Multimodal Concatenation

- Interleave visual tokens with textual tokens  
- Insert separator tokens  
- Generate unified token stream  

Output:

- Multimodal token stream

---

#### 5.3.4 Attention Mask Synthesis

- Construct causal mask  
- Construct cross-attention mask  
- Construct padding mask  

Output:

- Composite attention mask tensor

---

#### 5.3.5 Cross-Attention Conditioning

- Execute cross-attention layers  
- Weight visual context against textual context  
- Produce conditioned hidden states  

Output:

- Multimodal latent representation

---

### 5.4 Autoregressive Decoding Engine

Purpose: Generate structured table representation from latent space.

---

#### 5.4.1 Decoding Initialization

- Initialize decoder state  
- Load conditioning embeddings  
- Reset beam buffers  

---

#### 5.4.2 Token Generation Loop

For each decoding step:

1. Compute logits  
2. Apply temperature scaling  
3. Apply top-p filtering  
4. Apply logit biasing  
5. Sample next token  

---

#### 5.4.3 Stopping Criteria

- End-of-table token  
- Max token limit  
- Repetition threshold  

---

#### 5.4.4 Decoding Output

- Markdown table  
- CSV table  
- Confidence estimate  

---

## ✅ Structural Validation Phase

Purpose: Enforce strict syntactic, structural, semantic, and statistical integrity of extracted tabular representations before acceptance into the authoritative state.

This phase operates as a **hard-gate** in the pipeline.  
No downstream execution may occur unless this phase returns a passing verdict.

---

### 6.1 Syntax Integrity Validation Layer

Objective: Guarantee machine-parseable correctness.

Checks:

- Markdown table grammar compliance  
- CSV grammar compliance  
- Proper delimiter usage  
- Balanced pipe characters  
- Proper header separator row  
- Escaping correctness for special characters  

Failure Conditions:

- Malformed rows  
- Unequal column counts  
- Illegal tokens  

---

### 6.2 Schema Compliance Validation Layer

Objective: Enforce rectangular matrix topology.

Checks:

- Uniform column cardinality across all rows  
- Presence of header row  
- Absence of ragged rows  
- No null structural cells  

Failure Conditions:

- Missing cells  
- Extra cells  
- Header mismatch  

---

### 6.3 Semantic Coherence Validation Layer

Objective: Ensure column meaning consistency.

Checks:

- Header stability across retries  
- Data type coherence per column  
- Numeric plausibility  
- Unit consistency  
- Category value consistency  

Failure Conditions:

- Mixed datatypes in same column  
- Invalid numeric values  
- Header drift  

---

### 6.4 Statistical Integrity Validation Layer

Objective: Detect pathological outputs.

Checks:

- Shannon entropy threshold  
- Cell density threshold  
- Duplicate ratio  
- Outlier ratio  

Failure Conditions:

- Entropy too low → likely hallucination  
- Entropy too high → likely noise  

---

### 6.5 Cross-Format Equivalence Validation

Objective: Ensure Markdown and CSV representations encode identical data.

Checks:

- Parse Markdown → matrix  
- Parse CSV → matrix  
- Cell-by-cell equivalence  

Failure Conditions:

- Any mismatch  

---

## 🔁 Recursive Repair Loop

Purpose: Automatically recover from validation or QC failures and maximize table extraction fidelity.  
This loop is **agent-driven**, **stateful**, and **retry-aware**, ensuring controlled convergence without infinite cycling.

---

### 7.1 Repair Strategy Selection Engine

The engine evaluates failure causes and selects repair strategies dynamically:

- **Alternate Preprocessing Path**  
  - Switch between photometric, geometric, or morphological normalization graphs  
- **Prompt Mutation**  
  - Adjust instruction phrasing for VLM  
  - Modify table description, hints, or layout emphasis  
- **Temperature Annealing Adjustment**  
  - Increase temperature for more diverse token exploration  
  - Decrease for conservative decoding  
- **Region Expansion or Contraction**  
  - Crop or pad candidate regions  
  - Adjust bounding boxes based on line density analysis  
- **Vision Embedding Re-sampling**  
  - Re-extract patches or features  
  - Emphasize edges or suppress noise  
- **Line Emphasis Boost**  
  - Reinforce detected horizontal/vertical lines  
  - Morphological dilation of table borders  
- **Noise Attenuation Boost**  
  - Apply additional denoising filters  
  - Enhance structural clarity  

Output:

- Selected repair path ID  
- Estimated efficacy score  

---

### 7.2 Repair Execution Cycle

Steps:

1. Apply selected repair strategy to candidate region  
2. Re-run **Vision-Language Inference Phase**  
3. Re-run **Structural Validation Phase**  
4. Record success/failure and updated confidence  

Each cycle produces a **new candidate table state**, tagged with:

- `retry_counter`  
- `lineage_id`  
- `failure_reasons`  
- `confidence_adjustment`  

---

### 7.3 Termination Policy

If maximum retries are reached without a valid output, the candidate is flagged for **manual review** and logged in telemetry.

---

### 7.4 Logging & Telemetry During Repair

Each retry logs:

- Inputs and outputs  
- Repair strategy applied  
- Validation and QC results  
- Confidence delta  
- Latency metrics  

This supports **auditability** and **post-mortem analysis**.

---

### 7.5 Retry State Visualization (Optional)

- Retry tree visualization  
- Branch success/failure heatmap  
- Confidence trajectory plot  

---

### 7.6 Repair Loop Outputs

Upon successful repair:

- Apply selected repair strategy

- Re-run VLM inference

- Re-run structural validation

---

## 🧪 Cross-Agent Quality Control Phase

**Purpose:** Independent verification of final candidate.

### 8.1 Heuristic Validation
- Hallucinated column detection
- Duplicate row detection
- Numeric monotonicity
- Total consistency
---

### 8.2 Statistical Cross-Check
- Distribution comparison
- Value range checking
---

## 🔀 State Convergence Phase

**Purpose:** Merge multiple candidates into authoritative table.

### 9.1 Candidate Alignment
- Row alignment
- Column alignment
---

### 9.2 Fusion Operations
- Cell majority voting
- Confidence-weighted averaging
- Semantic clustering

---

## 💾 Persistence Phase

**Purpose:** Store final artifacts.

### 10.1 Stored Artifacts
- Markdown
- CSV
- JSON
- Metadata
- Lineage graph
---

### 10.2 Storage Layout

data/final_tables/
- tables.md
- tables.csv
- tables.json
- metadata.json

---


## 📊 Telemetry & Tracing Phase

**Purpose:** Emit observability signals.

- Signals
- Inputs
- Outputs
- Latency
- Token counts
- Confidence
- Errors

---

## 📈 Evaluation Phase

**Purpose:** Quantify system performance.

### Metrics
- Cell accuracy
- Row recall
- Column precision
- Edit distance

**Stored in:** `experiments/`

---

## 🗂 Artifact Versioning Phase

**Artifacts tagged:** `table_v<major>.<minor>.<patch>`

## 🛑 Failure Containment Phase

| Failure Type       | Action         |
|------------------|----------------|
| VLM crash         | Reload model   |
| Validation fail   | Retry          |
| QC fail           | Retry          |
| Disk fail         | Cache          |
| OOM               | Chunk          |


---

## Author Notes

This repository reflects a research-driven seismic enhancement philosophy emphasizing interpretability, physical realism, and amplitude integrity over black-box performance.

# 🔒 Code Policy

Main application code and notebooks are intentionally excluded.

This repository contains:

    Project structure
    Documentation
    Templates

Contact the author for access to the full implementation.



