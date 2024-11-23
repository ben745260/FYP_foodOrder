import { OpenAI } from 'openai';

// const apiKey = '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';  // Replace with your actual OpenAI API key
const apiKey = import.meta.env.VITE_OPENAI_API_KEY;  // Replace with your actual OpenAI API key
const openai = new OpenAI({
  apiKey,
  dangerouslyAllowBrowser: true,
});

export async function generateDescription(productName,systemMsg,userMsg) {
  const messages = [
    { role: 'system', content: systemMsg},
    { role: 'user', content: userMsg },
    { role: 'assistant', content: productName },
  ];

  const chatMessages = messages.map((message) => ({
    role: message.role,
    content: message.content,
  }));

  try {
    const response = await openai.chat.completions.create({
      messages: chatMessages,
      model: 'gpt-3.5-turbo',
      max_tokens: 400,
      temperature: 0.7,
      stop: '\n',
      // assistant_id: 'asst_sCP7Ij19wJkgXya8tCRj4k9V',  // Replace with your actual Assistant ID
    });

    const assistantResponse = response.choices[0].message.content.trim();

    return assistantResponse;
  } catch (error) {
    console.error('Error:', error);
    // Handle the error appropriately (e.g., show an error message)
  }
}