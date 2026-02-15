import './globals.css';

export const metadata = {
  title: 'Organization Assistant',
  description: 'AI-powered assistant for your organization',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
