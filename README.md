# MovieMind: IMDB Sentiment Analysis with RNN

A streamlined web application that performs sentiment analysis on movie reviews using Recurrent Neural Networks (RNN).

## 🎯 Overview

MovieMind analyzes the sentiment of movie reviews using a Simple RNN model trained on the IMDB dataset. It classifies reviews as either positive or negative, providing confidence scores for predictions.

## 🛠️ Tech Stack

- **TensorFlow/Keras**: Deep learning model implementation
- **Streamlit**: Web interface
- **NumPy**: Numerical computations
- **Python 3.10+**: Core programming language

## 📁 Project Structure

```
moviemind/
├── main.py                 # Streamlit web application
├── simple_rnn_model.h5     # Trained RNN model
├── prediction.ipynb        # Model prediction notebook
├── embedding.ipynb         # Word embedding notebook
└── requirements.txt        # Project dependencies
```

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Vansh3140/IMDB-Movie-Review-Sentiment-Analysis.git
cd moviemind
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Open your browser and navigate to `http://localhost:8501`
3. Enter a movie review in the text area
4. Click "Classify" to see the sentiment analysis results

## 🎓 Model Architecture

- Input Layer: Embedding layer (vocabulary size x 32)
- Hidden Layer: Simple RNN with 32 units
- Output Layer: Dense layer with sigmoid activation
- Maximum sequence length: 500 words

## 📊 Performance

The model achieves:
- Accuracy: ~94% on IMDB test set
- Fast inference time: <1s per review
- Robust handling of varied review lengths

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

Project Link: https://github.com/Vansh3140/IMDB-Movie-Review-Sentiment-Analysis
