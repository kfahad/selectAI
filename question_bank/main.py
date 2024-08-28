from fastapi import FastAPI, Request
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

# Load the quantized model and pipeline
model_name = "EleutherAI/gpt-neo-1.3B"  # Replace with the chosen model
model = AutoModelForCausalLM.from_pretrained(model_name, load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

@app.post("/generate-questions")
async def generate_questions(request: Request):
    data = await request.json()
    paragraph = data.get("paragraph")
    
    # Generate questions using the model
    questions_and_answers = []
    
    # Example: Generate a question-answer pair based on the paragraph
    qa_input = {
        "context": paragraph,
        "question": "What is the main idea of the paragraph?"
    }
    answer = qa_pipeline(qa_input)
    questions_and_answers.append({
        "question": qa_input["question"],
        "answer": answer['answer']
    })
    
    return {"questions": questions_and_answers}
