'use client';

import { useState, useRef, useCallback } from 'react';
import ChatWindow from '../components/ChatWindow';
import { sendQuestion } from '../services/api';

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const textareaRef = useRef(null);

  const autoResize = () => {
    const el = textareaRef.current;
    if (!el) return;
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 120) + 'px';
  };

  const handleSubmit = useCallback(async (questionText) => {
    const question = (questionText || input).trim();
    if (!question || isLoading) return;

    setInput('');
    setError(null);
    if (textareaRef.current) textareaRef.current.style.height = 'auto';

    // Add user message
    const userMsg = {
      id: Date.now(),
      role: 'user',
      content: question,
      timestamp: new Date().toISOString(),
    };
    setMessages((prev) => [...prev, userMsg]);
    setIsLoading(true);

    try {
      const data = await sendQuestion(question);

      const botMsg = {
        id: Date.now() + 1,
        role: 'bot',
        content: data.answer,
        sources: data.sources || [],
        confidence: data.confidence,
        timestamp: new Date().toISOString(),
      };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      if (err.message === 'RATE_LIMIT') {
        setError('Too many requests. Please wait a moment and try again.');
      } else if (err.message === 'BAD_REQUEST') {
        setError('Invalid request. Please rephrase your question.');
      } else {
        setError('Something went wrong. Please try again.');
      }
    } finally {
      setIsLoading(false);
      textareaRef.current?.focus();
    }
  }, [input, isLoading]);

  const handleKey = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div
      className="relative flex flex-col h-screen max-w-[820px] mx-auto"
      style={{ zIndex: 1 }}
    >
      {/* Background gradient */}
      <div
        className="fixed inset-0 pointer-events-none"
        style={{
          background: `
            radial-gradient(ellipse 80% 50% at 20% -10%, rgba(124,106,247,0.12) 0%, transparent 60%),
            radial-gradient(ellipse 60% 40% at 80% 110%, rgba(249,127,110,0.07) 0%, transparent 60%)
          `,
          zIndex: 0,
        }}
      />

      {/* HEADER */}
      <header
        className="flex items-center justify-between px-7 py-[18px] flex-shrink-0"
        style={{
          borderBottom: '1px solid var(--border)',
          background: 'rgba(15,15,19,0.85)',
          backdropFilter: 'blur(16px)',
          position: 'relative',
          zIndex: 10,
        }}
      >
        {/* Logo - SAME PURPLE AS USER MESSAGE */}
        <div className="flex items-center gap-3">
          <div
            className="px-3 py-2 rounded-[10px] flex items-center justify-center text-[13px] font-bold text-white"
            style={{
              background: 'var(--accent)',  // CHANGED TO USE SAME COLOR
              boxShadow: '0 4px 20px rgba(124,106,247,0.3)',
              letterSpacing: '0.5px',
            }}
          >
            SSOGEN
          </div>
        </div>

        

        {/* Status */}
        <div className="flex items-center gap-2 text-[12.5px]" style={{ color: 'var(--text-muted)' }}>
          <span
            className="w-[7px] h-[7px] rounded-full animate-pulse-dot"
            style={{ background: '#4ade80', boxShadow: '0 0 8px rgba(74,222,128,0.6)' }}
          />
          Online
        </div>
      </header>

      {/* CHAT WINDOW */}
      <ChatWindow
        messages={messages}
        isLoading={isLoading}
        error={error}
        onSuggestion={handleSubmit}
      />

      {/* INPUT AREA */}
      <div
        className="px-6 pt-4 pb-5 flex-shrink-0"
        style={{
          borderTop: '1px solid var(--border)',
          background: 'rgba(15,15,19,0.9)',
          backdropFilter: 'blur(16px)',
          position: 'relative',
          zIndex: 10,
        }}
      >
        <div
          className="flex gap-2.5 items-end rounded-[16px] px-[18px] py-2.5 transition-all duration-200"
          style={{
            background: 'var(--surface-2)',
            border: '1px solid var(--border)',
          }}
          onFocus={(e) => {
            e.currentTarget.style.borderColor = 'var(--accent)';
            e.currentTarget.style.boxShadow = '0 0 0 3px rgba(124,106,247,0.18)';
          }}
          onBlur={(e) => {
            if (!e.currentTarget.contains(e.relatedTarget)) {
              e.currentTarget.style.borderColor = 'var(--border)';
              e.currentTarget.style.boxShadow = 'none';
            }
          }}
        >
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => { setInput(e.target.value); autoResize(); }}
            onKeyDown={handleKey}
            placeholder="Type your question here..."
            rows={1}
            disabled={isLoading}
            className="flex-1 bg-transparent border-none outline-none text-[14.5px] leading-[1.5] resize-none overflow-y-auto"
            style={{
              color: 'var(--text)',
              fontFamily: 'DM Sans, sans-serif',
              maxHeight: '120px',
              minHeight: '24px',
            }}
          />

          {/* Send button */}
          <button
            onClick={() => handleSubmit()}
            disabled={isLoading || !input.trim()}
            className="w-[38px] h-[38px] rounded-[10px] flex items-center justify-center flex-shrink-0 transition-all duration-200"
            style={{
              background: isLoading || !input.trim() 
                ? 'var(--surface)' 
                : 'var(--accent)',  // SAME COLOR AS LOGO
              boxShadow: isLoading || !input.trim() ? 'none' : '0 2px 12px rgba(124,106,247,0.35)',
              cursor: isLoading || !input.trim() ? 'not-allowed' : 'pointer',
              opacity: isLoading || !input.trim() ? 0.5 : 1,
            }}
          >
            <svg width="17" height="17" viewBox="0 0 24 24" fill="white">
              <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
            </svg>
          </button>
        </div>

        <p className="text-center text-[11px] mt-2" style={{ color: 'var(--text-dim)' }}>
          Press Enter to send &nbsp;·&nbsp; Shift+Enter for new line
        </p>
      </div>
    </div>
  );
}