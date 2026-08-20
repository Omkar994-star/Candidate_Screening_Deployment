import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "AI Candidate Screening",
  description: "Resume Based Intelligent Interview System",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}