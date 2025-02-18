import re

def generate_detailed_summary(text):
    """Generates a more detailed summary of a tax determination."""
    sentences = text.split('. ')
    if len(sentences) > 5:
        return '. '.join(sentences[:5]) + '...'  # Extracts 5 key sentences
    return text[:500] + '...'  # Default to first 500 characters

def rank_relevance(text, query):
    """Ranks document relevance based on query matching."""
    words = re.findall(r'\b\w+\b', query.lower())
    relevance_score = sum(text.lower().count(word) for word in words)
    return relevance_score  # Higher score means higher relevance

def extract_legal_references(text):
    """Extracts legal references like RCW and WAC codes from the document."""
    rcw_refs = re.findall(r"RCW\s\d{1,2}\.\d{1,3}(?:\.\d{1,3})?", text)
    wac_refs = re.findall(r"WAC\s\d{1,3}-\d{1,3}-\d{1,3}", text)
    return list(set(rcw_refs + wac_refs)) if rcw_refs or wac_refs else ["No specific legal references found"]

def explain_legal_references(references, text):
    """Provides explanations for legal references found in the document."""
    explanations = []
    
    reference_explanations = {
        "RCW 82.12.020": "Defines the use tax in Washington and when it applies.",
        "RCW 82.12.010": "Outlines what constitutes 'use' for tax purposes, including personal use of business assets.",
        "WAC 458-20-155": "Regulation explaining when digital products and software access are taxable.",
        "WAC 458-20-211": "Clarifies how employer-provided benefits (like vehicles) are taxed under use tax laws.",
        "WAC 458-20-15503": "Discusses taxability of digital goods and cloud-based software."
    }

    for ref in references:
        explanation = reference_explanations.get(ref, "No additional explanation available.")
        explanations.append(f"{ref}: {explanation}")

    return " | ".join(explanations) if explanations else "No explanations available."
