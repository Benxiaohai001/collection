use std::path::PathBuf;
use structopt::StructOpt;
use indicatif::{ProgressBar, ProgressStyle};


/// Command line arguments
#[derive(Debug, StructOpt)]
#[structopt(name = "line_protocol", about = "A line protocol tool.")]
struct Opt {
    /// Output file
    #[structopt(short = "o", parse(from_os_str))]
    output_file: PathBuf,

    /// Start timestamp
    #[structopt(long = "start")]
    start_timestamp: u64,

    /// End timestamp
    #[structopt(long = "end")]
    end_timestamp: u64,

    /// Interval in nanoseconds
    #[structopt(short = "i")]
    interval_nanoseconds: u64,
}

fn main() {
    let opt = Opt::from_args();
    println!("{:?}", opt);

    let total_size = opt.end_timestamp - opt.start_timestamp; // Replace this with your actual total size
    let pb = ProgressBar::new(total_size);
    pb.set_style(ProgressStyle::default_bar()
        .template("{spinner:.green} [{elapsed_precise}] [{bar:40.cyan/blue}] {bytes}/{total_bytes} ({eta})")
        .progress_chars("#>-"));

    for _ in opt.start_timestamp..opt.end_timestamp {
        // Your logic here

        pb.inc(opt.interval_nanoseconds); // Increase the progress bar
    }

    pb.finish_with_message("done");
}



