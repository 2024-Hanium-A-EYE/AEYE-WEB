import type { Metadata } from "next";
import Pretendard from "@/styles/local-font";

import "@/styles/globals.css";

export const metadata: Metadata = {
  title: "AEYE - 로그인",
  description: "AEYE 로그인 페이지",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <body className={Pretendard.className}>{children}</body>
    </html>
  );
}
