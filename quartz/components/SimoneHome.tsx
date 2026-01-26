import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/simonehome.scss"

export default (() => {
    const SimoneHome: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
        return (
            <div class={`simone-home ${displayClass ?? ""}`}>

                {/* HERO SECTION */}
                <section class="hero">
                    <div class="hero-content">
                        <h1>Simone Testino</h1>
                        <p class="tagline">
                            Mathematician • Philosopher • Entrepreneur
                        </p>
                        <div class="contact-bar">
                            <a href="mailto:simone.testino@gmail.com" class="contact-link">📧 simone.testino@gmail.com</a>
                            <a href="https://wa.me/393396379372" class="contact-link">💬 +39 339 637 9372</a>
                            <a href="https://github.com/SimoneTestino" class="contact-link">🐙 GitHub</a>
                        </div>
                        <div class="quick-links">
                            <a href="/Academia/Active--and--Works/Curriculum-Vitae.pdf" class="link-pill">CV</a>
                            <a href="/System/Contacts/Contacts" class="link-pill">Contacts</a>
                            <a href="/System/Condensed-Biography" class="link-pill">Biography</a>
                        </div>
                    </div>
                </section>

                {/* ABOUT ME */}
                <section class="about-section">
                    <h2>About Me</h2>
                    <div class="about-content">
                        <p>
                            I am a researcher working at the intersection of <strong>mathematics</strong> and <strong>philosophy</strong>,
                            with a particular focus on the foundations of mathematics, logic, and formal methods.
                            This website serves as an extension of my academic portfolio, providing a detailed
                            overview of my research, writings, and entrepreneurial ventures.
                        </p>
                    </div>
                </section>

                {/* RESEARCH AREAS */}
                <section class="research-section">
                    <h2>Research Areas</h2>
                    <p class="section-intro">
                        My research spans foundational mathematics and philosophy. Below are the specific fields where I have developed expertise and active research.
                    </p>
                    <div class="research-grid">
                        <div class="research-column">
                            <h3>Mathematics</h3>
                            <ul class="research-list">
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Set-Theory">Set Theory</a></li>
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Model-Theory">Model Theory</a></li>
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Modal-Logic">Modal Logic</a></li>
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Category-Theory">Category Theory</a></li>
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Algebra">Algebra</a></li>
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Translation-Theory">Translation Theory</a></li>
                            </ul>
                        </div>
                        <div class="research-column">
                            <h3>Philosophy</h3>
                            <ul class="research-list">
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Philosophy-of-Mathematics-and-Logic">Philosophy of Mathematics & Logic</a></li>
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Metaphysics--and--Ontology">Metaphysics & Ontology</a></li>
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Formal-Epistemology">Formal Epistemology</a></li>
                                <li><a href="/Academia/Active--and--Works/Research-Areas/Formal-Cognitive-Sciences">Formal Cognitive Sciences</a></li>
                            </ul>
                        </div>
                    </div>
                </section>

                {/* ACADEMIC WORK */}
                <section class="academia-section">
                    <h2>Academic Work</h2>
                    <div class="academia-grid">
                        <a href="/Academia/Active--and--Works/Academic-Writings" class="academia-card">
                            <span class="card-icon">📝</span>
                            <h3>Academic Writings</h3>
                            <p>Essays, thoughts, and writings related to my research areas</p>
                        </a>
                        <a href="/Academia/Notes--and--Papers/Notes--and--Papers" class="academia-card">
                            <span class="card-icon">📚</span>
                            <h3>Notes & Papers</h3>
                            <p>Papers I have read with comments, and lecture notes</p>
                        </a>
                        <a href="/Academia/Active--and--Works/Academic-Diary" class="academia-card">
                            <span class="card-icon">📓</span>
                            <h3>Academic Diary</h3>
                            <p>Notes and decisions regarding my academic life</p>
                        </a>
                        <a href="/Academia/Active--and--Works/Academic-Diary/2024/PhD-Applications/PhD-Applications" class="academia-card">
                            <span class="card-icon">🎓</span>
                            <h3>PhD Applications</h3>
                            <p>Documentation of my doctoral application process</p>
                        </a>
                    </div>
                </section>

                {/* MASTER THESIS */}
                <section class="thesis-section">
                    <h2>Master Thesis</h2>
                    <div class="thesis-card">
                        <div class="thesis-header">
                            <span class="thesis-icon">📜</span>
                            <div class="thesis-meta">
                                <h3>Translation Theory</h3>
                                <span class="thesis-degree">MSc Logic — University of Amsterdam</span>
                            </div>
                        </div>
                        <div class="thesis-details">
                            <div class="thesis-info">
                                <span class="info-label">Supervisor:</span>
                                <span class="info-value">TBD</span>
                            </div>
                            <div class="thesis-info">
                                <span class="info-label">Timeline:</span>
                                <span class="info-value">January 2026 — August 2026</span>
                            </div>
                            <p class="thesis-description">
                                Research on translation theory in mathematical logic, planned to begin in January 2026
                                with the goal of submission and defence in August 2026, completing my MSc Logic degree.
                            </p>
                        </div>
                        <a href="/Academia/Active--and--Works/Master/6th-Semester/Master-Thesis" class="thesis-link">
                            View Thesis Details →
                        </a>
                    </div>
                </section>

                {/* FINANCIALS */}
                <section class="financials-section">
                    <h2>Financial Life</h2>
                    <p class="section-intro">
                        Documentation of my financial management, investments, and personal finance strategies.
                    </p>
                    <div class="utilities-grid">
                        <a href="/Personal-Finance/Personal-Finance" class="utility-link">
                            <span>💹</span> Personal Finance
                        </a>
                        <a href="/Personal-Finance/Investments" class="utility-link">
                            <span>📈</span> Investments
                        </a>
                        <a href="/Personal-Finance/Financial-Diary" class="utility-link">
                            <span>📒</span> Financial Diary
                        </a>
                        <a href="https://testinofinance.pages.dev/" target="_blank" class="utility-link">
                            <span>📊</span> Finance Dashboard
                        </a>
                    </div>
                </section>

                {/* COLIVINGLIGURIA */}
                <section class="cl-block">
                    <div class="cl-content">
                        <div class="cl-badge">🏡 Venture</div>
                        <h2>ColivingLiguria</h2>
                        <p>
                            A venture transforming historic Ligurian villas into hubs for remote workers,
                            creatives, and digital nomads. We combine the charm of 1920s architecture
                            with 2025 technology to create a unique coliving experience.
                        </p>
                        <div class="cl-features">
                            <span class="feature-tag">Remote Work</span>
                            <span class="feature-tag">Community Living</span>
                            <span class="feature-tag">Historic Renovation</span>
                            <span class="feature-tag">Digital Nomads</span>
                        </div>
                        <a href="https://colivingliguria.pages.dev" target="_blank" class="cl-button">
                            Visit ColivingLiguria →
                        </a>
                    </div>
                </section>

                {/* LUNA */}
                <section class="luna-block">
                    <div class="luna-content">
                        <div class="luna-logo">L</div>
                        <h2>Luna</h2>
                        <p>
                            A manufacturing startup developing revolutionary helium balloon lighting systems.
                            Compared to traditional light towers, Luna delivers superior performance at a
                            fraction of the weight and cost.
                        </p>
                        <div class="luna-stats">
                            <div class="stat">
                                <span class="stat-value">2×</span>
                                <span class="stat-label">The Light</span>
                            </div>
                            <div class="stat">
                                <span class="stat-value">&lt;0.5kg</span>
                                <span class="stat-label">Weight</span>
                            </div>
                            <div class="stat">
                                <span class="stat-value">⅓</span>
                                <span class="stat-label">The Cost</span>
                            </div>
                        </div>
                        <a href="https://lunalighting.pages.dev" target="_blank" class="luna-button">
                            Explore Luna →
                        </a>
                    </div>
                </section>

                {/* UTILITIES */}
                <section class="utilities-section">
                    <h2>Website Utilities</h2>
                    <div class="utilities-grid">
                        <a href="https://cal.com/simone.testino/" target="_blank" class="utility-link">
                            <span>📞</span> Book a Call
                        </a>
                        <a href="https://wa.me/393396379372" target="_blank" class="utility-link">
                            <span>💬</span> WhatsApp
                        </a>
                        <a href="mailto:simone.testino@gmail.com" class="utility-link">
                            <span>📧</span> Email
                        </a>
                        <a href="/System/Contacts/Contacts" class="utility-link">
                            <span>👤</span> Contacts
                        </a>
                        <a href="/System/Contacts/Availability" class="utility-link">
                            <span>📅</span> Availability
                        </a>
                        <a href="/System/Contacts/Payment-Methods" class="utility-link">
                            <span>💳</span> Payment Methods
                        </a>
                        <a href="/System/Documents" class="utility-link">
                            <span>📄</span> Documents
                        </a>
                    </div>
                </section>

            </div>
        )
    }

    SimoneHome.css = style
    return SimoneHome
}) satisfies QuartzComponentConstructor
