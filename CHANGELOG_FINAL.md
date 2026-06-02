# Changelog - Rascadores Cali Chatbot

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.5.0] - 2026-06-02

### Status
✅ **PRODUCTION** | Ready for deployment

### Summary
Major release resolving overfitting issues and semantic misclassification from v1.0-v1.4. Introduces class weight balancing, optimized architecture, and ONNX export for web deployment.

### Added
- **ONNX Export Pipeline**: Model exported to `chatbot_model_v1.5.onnx` with external weights file
- **Metadata JSON**: `metadata_v4.json` containing vocabulary and response mappings
- **Classification Metrics**: Full `classification_report` with per-intent precision/recall/F1-score
- **Generalization Diagnostics**: Edge-case testing to validate semantic understanding
- **Training Visualization**: Loss progression and convergence analysis (log-scale)
- **Web Deployment Ready**: ONNX Runtime compatibility (browser + Node.js)

### Fixed
- **Semantic Confusion**: 'gato_grande_pesado' no longer misclassified as 'pago'
  - Root cause: Model unable to distinguish weight-related vs payment contexts
  - Solution: Custom class weighting (3.0) for 'gato_grande_pesado'
  - Validation: Precision 0.98, Recall 0.97 post-fix

- **Overfitting**: 99%+ training accuracy with poor generalization
  - Root cause: Architecture overcapacity (256 hidden neurons) + no regularization
  - Solution: Reduced to 16 neurons, added dropout (0.2)
  - Impact: Generalization gap closed (98.6% consistent accuracy)

### Changed
- **Architecture**: 
  - Hidden layer size: 256 → 16 neurons
  - Rationale: Prevent memorization, force semantic understanding
  
- **Regularization**:
  - Dropout: 0.0 → 0.2
  - Loss function: Standard CrossEntropyLoss → Weighted CrossEntropyLoss
  
- **Training Parameters**:
  - Epochs: 100 → 300 (ensure convergence)
  - Learning rate: 0.002 → 0.001 (more stable descent)
  - Optimizer: AdamW → Adam (simpler for this scale)

### Metrics
```
Final Accuracy: 98.6%
Training Stability: ✓ No divergence
Generalization: ✓ Stable across all intents

Per-Intent Performance (sample):
  - saludo:                  precision=1.00, recall=1.00, f1=1.00
  - gato_grande_pesado:      precision=0.98, recall=0.97, f1=0.98 (FIXED)
  - consulta_precio:         precision=0.97, recall=0.96, f1=0.96
  - envios:                  precision=0.97, recall=0.98, f1=0.97
  - pagos:                   precision=0.95, recall=0.96, f1=0.95
  
  Weighted Avg: precision=0.96, recall=0.96, f1=0.96
```

### Technical Details
- **Model Size**: ~50KB ONNX + weights
- **Inference Latency**: <5ms (CPU)
- **Deployment**: Client-side (no backend required)
- **Framework**: PyTorch 1.x, ONNX opset 14

### Artifacts
- `chatbot_model_v1.5.onnx` - Model definition
- `chatbot_model_v1.5.onnx.data` - Model weights
- `metadata_v4.json` - Vocabulary and response mappings
- `training_curves/` - Loss and convergence visualizations
- `classification_report.txt` - Detailed metrics

---

## [1.4.0] - 2026-05-XX (Experimental)

### Status
⚠️ **EXPERIMENTAL** | Known issues

### Issues
- Overfitting: 99%+ train accuracy, <80% edge-case generalization
- Semantic confusion: 'gato_grande_pesado' ↔ 'pago' misclassification
- Architecture: 256 hidden neurons (excess capacity)
- No regularization or class weighting

### Notes
- Attempted increased dropout, but issue persisted
- Root cause analysis: architecture too large for dataset size
- Decision: Pivot to v1.5 with reduced capacity + weighted loss

---

## [1.3.0] - 2026-05-XX (Experimental)

### Status
⚠️ **EXPERIMENTAL** | Still experiencing overfitting

### Changed
- Added Batch Normalization attempt
- Increased regularization attempts
- Did not resolve underlying semantic confusion

### Notes
- Issue remained: gato_grande_pesado confusion
- Realized hyperparameter tuning alone insufficient
- Architecture redesign needed (v1.5)

---

## [1.2.0] - 2026-05-XX (Experimental)

### Status
⚠️ **EXPERIMENTAL** | High overfitting observed

### Changed
- Increased dataset size and intent variety
- Attempted batch-level optimizations
- Still observing train/test gap

---

## [1.1.0] - 2026-05-XX (Experimental)

### Status
⚠️ **EXPERIMENTAL** | Initial prototype

### Added
- Basic 4-layer MLP architecture
- NLTK tokenization + stemming
- Bag-of-Words encoding
- 38+ intent categories

### Known Issues
- Severe overfitting (99%+ train, poor gen.)
- Semantic confusion not diagnosed yet

---

## [1.0.0] - 2026-04-XX (Experimental)

### Status
⚠️ **EXPERIMENTAL** | Proof of concept

### Added
- Initial chatbot training pipeline
- Simple linear models (no hidden layers)
- Basic intent classification

### Known Issues
- Insufficient model capacity
- No generalization testing

---

## Versioning Strategy

### Semantic Versioning Used
- **MAJOR** (1.x.0): Architecture or paradigm changes
- **MINOR** (x.1.0): Feature additions or optimization improvements
- **PATCH** (x.x.1): Bug fixes or tiny hyperparameter tweaks

### Release Types
- ✅ **PRODUCTION**: Stable, tested, delivered to client
- ⚠️ **EXPERIMENTAL**: Development iterations, not production-ready
- 🔧 **DEPRECATED**: Superseded, do not use

### Timeline Summary
```
v1.0-1.4: Experimental phase (4-5 iterations)
           └─ Problem: Overfitting + semantic confusion
           
v1.5:     Production phase (FINAL)
           └─ Solution: Architecture redesign + class weighting
           └─ Status: Deployed to Rascadores Cali ✓
```

---

## Notes for Future Versions

### Potential v1.6 (Post-Production)
- [ ] Fine-tune with real customer conversations
- [ ] Add intent confidence threshold tuning
- [ ] Implement context memory (multi-turn dialogues)
- [ ] Expand to 50+ intents if needed

### Potential v2.0 (Major Redesign)
- [ ] Move to transformer-based architecture (BERT, DistilBERT)
- [ ] Add semantic similarity matching
- [ ] Support multi-language (es, en, pt)
- [ ] Implement feedback loop for continuous learning

---

**Last Updated**: 2026-06-02  
**Maintained By**: Santiago (Smart Systems SSS)  
**Client**: Rascadores Cali
