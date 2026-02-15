export default function MessageBubble({ message }) {
  const isUser = message.role === 'user';
  const time = new Date(message.timestamp).toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit',
  });

  return (
    <div className={`flex gap-3 animate-fade-slide ${isUser ? 'flex-row-reverse' : ''}`}>
      {/* Avatar - SWAPPED COLORS */}
      <div
        className="w-[34px] h-[34px] rounded-full flex items-center justify-center text-sm font-semibold flex-shrink-0 mt-0.5 text-white"
        style={{
          background: isUser
            ? 'linear-gradient(135deg, #7c6af7, #9d8fff)'  // User now has purple (was bot color)
            : 'linear-gradient(135deg, #f97f6e, #fb9d5e)',  // Bot now has orange (was user color)
          boxShadow: isUser ? '0 0 14px rgba(124,106,247,0.18)' : 'none',
        }}
      >
        ⚡
      </div>

      {/* Bubble */}
      <div className={`flex flex-col gap-1 max-w-[72%] ${isUser ? 'items-end' : ''}`}>
        <div
          className="px-[17px] py-[13px] text-[14.5px] leading-[1.65] break-words rounded-[18px]"
          style={
            isUser
              ? {
                  background: 'var(--accent)',
                  borderTopRightRadius: '4px',
                  color: '#fff',
                  boxShadow: '0 4px 20px rgba(124,106,247,0.3)',
                }
              : {
                  background: 'var(--surface-2)',
                  border: '1px solid var(--border)',
                  borderTopLeftRadius: '4px',
                  color: 'var(--text)',
                }
          }
        >
          {/* Message text */}
          <p style={{ whiteSpace: 'pre-wrap' }}>{message.content}</p>
        </div>

        {/* Timestamp */}
        <span className="text-[11px] px-1" style={{ color: 'var(--text-dim)' }}>
          {time}
        </span>
      </div>
    </div>
  );
}