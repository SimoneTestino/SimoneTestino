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
                            <a href="/Academia/Active-&-Works/Curriculum-Vitae.pdf" class="link-pill">CV</a>
                            <a href="/System/This-Website/Contacts" class="link-pill">Contacts</a>
                            <a href="/System/This-Website/Condensed-Biography" class="link-pill">Biography</a>
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
                        My research spans foundational mathematics and philosophy, with expertise developed across the following fields.
                    </p>
                    <div class="research-grid">
                        <div class="research-column">
                            <h3>Mathematics</h3>
                            <ul class="research-list">
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Set-Theory">Set Theory</a></li>
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Model-Theory">Model Theory</a></li>
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Modal-Logic">Modal Logic</a></li>
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Category-Theory">Category Theory</a></li>
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Algebra">Algebra</a></li>
                            </ul>
                        </div>
                        <div class="research-column">
                            <h3>Philosophy</h3>
                            <ul class="research-list">
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Philosophy-of-Mathematics-and-Logic">Philosophy of Mathematics & Logic</a></li>
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Metaphysics-&-Ontology">Metaphysics & Ontology</a></li>
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Formal-Epistemology">Formal Epistemology</a></li>
                                <li><a href="/Academia/Active-&-Works/Research-Areas/Formal-Cognitive-Sciences">Formal Cognitive Sciences</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="research-cta">
                        <a href="/Academia/Active-&-Works/Research-Areas/Research-Areas" class="link-pill">View All Research Areas →</a>
                    </div>
                </section>

                {/* ACADEMIC WORK */}
                <section class="academia-section">
                    <h2>Academic Work</h2>
                    <div class="academia-grid">
                        <a href="/Academia/Active-&-Works/Academic-Writings" class="academia-card">
                            <span class="card-icon">📝</span>
                            <h3>Academic Writings</h3>
                            <p>Essays, thoughts, and writings related to my research areas</p>
                        </a>
                        <a href="/Academia/Notes-&-Papers" class="academia-card">
                            <span class="card-icon">📚</span>
                            <h3>Notes & Papers</h3>
                            <p>Papers I have read with comments, and lecture notes</p>
                        </a>
                        <a href="/Academia/Active-&-Works/Academic-Diary" class="academia-card">
                            <span class="card-icon">📓</span>
                            <h3>Academic Diary</h3>
                            <p>Notes and decisions regarding my academic life</p>
                        </a>
                        <a href="/Academia/Active-&-Works/PhD-Applications" class="academia-card">
                            <span class="card-icon">🎓</span>
                            <h3>PhD Applications</h3>
                            <p>Documentation of my doctoral application process</p>
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
                            Delivering 100,000 lumens from under 2kg at heights up to 50 metres—at a
                            fraction of traditional costs.
                        </p>
                        <div class="luna-stats">
                            <div class="stat">
                                <span class="stat-value">100k</span>
                                <span class="stat-label">Lumens</span>
                            </div>
                            <div class="stat">
                                <span class="stat-value">&lt;2kg</span>
                                <span class="stat-label">Weight</span>
                            </div>
                            <div class="stat">
                                <span class="stat-value">€750</span>
                                <span class="stat-label">Cost</span>
                            </div>
                        </div>
                        <a href="https://luna-st.pages.dev" target="_blank" class="luna-button">
                            Explore Luna →
                        </a>
                    </div>
                </section>

                {/* UTILITIES */}
                <section class="utilities-section">
                    <h2>Website Utilities</h2>
                    <div class="utilities-grid">
                        <a href="/System/This-Website/Contacts" class="utility-link">
                            <span>📧</span> Contacts
                        </a>
                        <a href="/System/This-Website/Availability" class="utility-link">
                            <span>📅</span> Availability
                        </a>
                        <a href="/System/This-Website/Payment-Methods" class="utility-link">
                            <span>💳</span> Payment Methods
                        </a>
                        <a href="/System/This-Website/Documents" class="utility-link">
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
