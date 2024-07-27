import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  console.log("req url pathname:", request.nextUrl.pathname);
  if (request.nextUrl.pathname === "/") {
    const url = request.nextUrl.clone();
    url.pathname = "/patients";
    return NextResponse.redirect(url);
  } else NextResponse.next();
}
