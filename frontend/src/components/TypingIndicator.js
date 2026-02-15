export default function TypingIndicator() {
  return (
    <div className="flex gap-3 items-start animate-fade-slide">
      {/* Avatar */}
      <div
        className="w-[34px] h-[34px] rounded-full flex items-center justify-center text-sm flex-shrink-0 mt-0.5 text-white"
        style={{
          background: 'linear-gradient(135deg, #7c6af7, #9d8fff)',
          boxShadow: '0 0 14px rgba(124,106,247,0.18)',
        }}
      >
        ⚡
      </div>

      {/* Typing bubbles */}
      <div
        className="flex gap-1.5 items-center px-[18px] py-[14px] rounded-[18px] rounded-tl-[4px]"
        style={{ background: 'var(--surface-2)', border: '1px solid var(--border)' }}
      >
        <div className="typing-dot" />
        <div className="typing-dot" />
        <div className="typing-dot" />
      </div>
    </div>
  );
}
