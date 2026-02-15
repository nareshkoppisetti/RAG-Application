'use client';

import { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
import TypingIndicator from './TypingIndicator';

const SUGGESTIONS = [
  'What is SSO?',
  'Oracle EBS integration',
  'PeopleSoft SSO setup',
  'SAML configuration',
];

export default function ChatWindow({ messages, isLoading, error, onSuggestion }) {
  const bottomRef = useRef(null);

  // Auto-scroll to bottom on new messages
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  const isEmpty = messages.length === 0;

  return (
    <div className="flex-1 overflow-y-auto px-6 py-7 flex flex-col gap-5">

      {/* Welcome Screen */}
      {isEmpty && !isLoading && (
        <div className="flex-1 flex flex-col items-center justify-center text-center gap-4 py-10">
          <div
            className="w-16 h-16 rounded-[20px] flex items-center justify-center text-3xl animate-float"
            style={{
              background: 'linear-gradient(135deg, #7c6af7, #9d8fff)',
              boxShadow: '0 0 40px rgba(124,106,247,0.18)',
            }}
          >
            💬
          </div>

          <h2
            className="text-[26px] tracking-tight"
            style={{ fontFamily: 'DM Serif Display, serif', color: 'var(--text)' }}
          >
            How can I help you?
          </h2>

          <p className="text-[14.5px] max-w-[340px] leading-relaxed" style={{ color: 'var(--text-muted)' }}>
            Ask me anything about our products, services, integrations, or documentation.
          </p>

          {/* Suggestion chips */}
          <div className="flex flex-wrap gap-2 justify-center mt-2">
            {SUGGESTIONS.map((s) => (
              <button
                key={s}
                onClick={() => onSuggestion(s)}
                className="px-4 py-2 rounded-full text-[13px] transition-all duration-200 cursor-pointer"
                style={{
                  background: 'var(--surface-2)',
                  border: '1px solid var(--border)',
                  color: 'var(--text-muted)',
                  fontFamily: 'DM Sans, sans-serif',
                }}
                onMouseEnter={(e) => {
                  e.target.style.borderColor = 'var(--accent)';
                  e.target.style.color = 'var(--text)';
                  e.target.style.background = 'rgba(124,106,247,0.1)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.borderColor = 'var(--border)';
                  e.target.style.color = 'var(--text-muted)';
                  e.target.style.background = 'var(--surface-2)';
                }}
              >
                {s}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Messages */}
      {messages.map((msg) => (
        <MessageBubble key={msg.id} message={msg} />
      ))}

      {/* Typing indicator */}
      {isLoading && <TypingIndicator />}

      {/* Error message */}
      {error && (
        <div
          className="rounded-[10px] px-4 py-2.5 text-[13.5px] text-center animate-fade-slide"
          style={{
            background: 'rgba(249,127,110,0.1)',
            border: '1px solid rgba(249,127,110,0.3)',
            color: '#f97f6e',
          }}
        >
          {error}
        </div>
      )}

      <div ref={bottomRef} />
    </div>
  );
}
