import { OpenAI } from 'openai';

// Replace with your actual API key
const apiKey = 'YOUR_API_KEY';

// Initialize the OpenAI client
const openai = new OpenAI({
  apiKey,
  dangerouslyAllowBrowser: true, // Allow usage in the browser
});

// Function to post chat messages
export async function postChatMessage(assistantId, userMessage) {
  try {
    // Create a thread for the chat
    const thread = await openai.assistants.createThread({
      model: 'gpt-4-turbo-preview', // Choose the appropriate model
    });

    // Append user message to the thread
    await openai.assistants.appendMessage(thread.id, {
      role: 'user',
      content: userMessage,
    });

    // Run the assistant to generate a response
    const response = await openai.assistants.run(thread.id);

    // Extract the assistant's response
    const assistantResponse = response.choices[0].message.content.trim();

    return assistantResponse;
  } catch (error) {
    console.error('Error posting chat message:', error);
    // Handle the error appropriately (e.g., show an error message)
    return 'An error occurred while processing the request.';
  }
}

// Example usage:
const myAssistantId = 'asst_sCP7Ij19wJkgXya8tCRj4k9V'; // Replace with your actual Assistant ID
const userMessage = 'Hello, can you recommend a vegetarian dish?';

const chatResponse = await postChatMessage(myAssistantId, userMessage);
console.log('Assistant response:', chatResponse);
